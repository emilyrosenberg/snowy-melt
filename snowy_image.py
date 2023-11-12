def snowy_image(tries):
    snowy = [
        """
            *     *   *   
        *      *    *
          *      *      *
        *      *      *
        ---------------
        """,
        """
           _|=|_
        -----------
        """,
        """
           _|=|_
           ('<')
        -----------
        """,
        """
           _|=|_
           ('<')
        >—(  o  )—<
        -----------
        """,
        """
           _|=|_
           ('<')
        >—(  o  )—<
         (   o   )
        -----------
        """,
        """
           _|=|_
           ('<')
        >—(  o  )—<
         (   o   )
        (    o    )
        -----------
        """
    ]
    return snowy[tries]